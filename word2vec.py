import numpy as np
import torch
import torch.nn.functional as F
corpus = [
    'he is a king',
    'she is a queen',
    'he is a man',
    'she is a woman',
    'warsaw is poland capital',
    'berlin is germany capital',
    'paris is france capital',
]

def tokenize_corpus(corpus):
    tokens = [x.split() for x in corpus]
    return tokens

tokenized_corpus = tokenize_corpus(corpus)

#print('tokenized_corpus: ', tokenized_corpus)

vocabulary = []
for sentence in tokenized_corpus:
    for token in sentence:
        if token not in vocabulary:
            vocabulary.append(token)
            
#print('vocabulary: ', vocabulary)

word2idx = {w: idx for (idx, w) in enumerate(vocabulary)}
idx2word = {idx: w for (idx, w) in enumerate(vocabulary)}

#print('word2idx: ', word2idx)
#print('idx2word: ', idx2word)

vocabulary_size = len(vocabulary)
#print('vocabulary_size: ', vocabulary_size)

window_size = 2
idx_pairs = []
#for each sentence
for sentence in tokenized_corpus:
    #print('sentence: ', sentence)
    indices = [word2idx[word] for word in sentence]
    #print('indices: ', indices)
    #for each word treated as center word
    for center_word_pos in range(len(indices)):
        #print('center_word_pos: ', center_word_pos)
        #for each window  position
        for w in range(-window_size, window_size+1):
            #print('w: ', w)
            context_word_pos = center_word_pos + w
            #print('center_word_pos and context_word_pos: ', center_word_pos,  context_word_pos)
            #make sure we dont jump out of the sentence
            if context_word_pos < 0 or context_word_pos >= len(indices) or center_word_pos == context_word_pos:
                continue
            context_word_idx = indices[context_word_pos]
            #print(context_word_idx)
            idx_pairs.append((indices[center_word_pos], context_word_idx))
            print(indices[center_word_pos], context_word_idx)
            
            #print('------')
        #print('==================')
    #print('**************')
    #exit()
    
idx_pairs = np.array(idx_pairs)

print(idx_pairs)
    
    
    
##################SWITCHING ON THE TORCH####################    

def get_input_layer(word_idx):
    x=torch.zeros(vocabulary_size).float()
    x[word_idx] = 1.
    return x

embedding_dims = 5
W1 = torch.randn(embedding_dims, vocabulary_size, requires_grad=True).float()
W2 = torch.randn(vocabulary_size, embedding_dims, requires_grad=True).float()
num_epochs = 200
lr = 0.001

for epo in range(num_epochs):
    loss_val = 0
    for data, target in idx_pairs:
        #print(data,type(target), type(data), target)
        x = get_input_layer(data)
        y_true = torch.from_numpy(np.array([target])).long()
        
        #print(x)
        #print(y_true)
        
        z1 = torch.matmul(W1, x)
        #print(x.shape)
        #print(W1.shape)
        #print(z1.shape)
        z2 = torch.matmul(W2, z1)
        #print(z2.shape)
        
        log_softmax = F.log_softmax(z2, dim = 0)
        #print(log_softmax.shape)
        loss = F.nll_loss(log_softmax.view(1, -1), y_true)
        #print(loss)
        loss_val += loss.data
        #print(loss_val)
        
        
        loss.backward()
        W1.data -= lr*W1.grad.data
        W2.data -= lr*W2.grad.data        
        
        W1.grad.data.zero_()
        W2.grad.data.zero_()
        
        
        #if epo % 10 == 0:    
            #print(loss_val)
            #print('Loss at epo {epo}: {loss_val/len(idx_pairs)}')
        #exit()
    print(loss_val)
    print('............')
    
    #exit()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    

import torch
import torch.nn as nn
import torch.nn.functional as F

class NCrossEmbeddingMatcher(nn.Module):
    def __init__(self, input_dim, embedding_dim):
        super().__init__()
        self.product_encoder = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, embedding_dim)
        )
        self.similarity_metrics = [
            self.cosine_similarity,
            self.euclidean_similarity,
            self.manhattan_similarity
        ]
    
    def forward(self, product1, product2):
        embed1 = self.product_encoder(product1)
        embed2 = self.product_encoder(product2)
        similarities = [
            metric(embed1, embed2) for metric in self.similarity_metrics
        ]
        final_similarity = self.aggregate_similarities(similarities)
        return final_similarity
    
    def cosine_similarity(self, embed1, embed2):
        return F.cosine_similarity(embed1, embed2)
    
    def euclidean_similarity(self, embed1, embed2):
        return -torch.norm(embed1 - embed2, dim=-1)
    
    def manhattan_similarity(self, embed1, embed2):
        return -torch.sum(torch.abs(embed1 - embed2), dim=-1)
    
    def aggregate_similarities(self, similarities):
        weights = torch.tensor([...])
        return torch.sum(torch.stack(similarities) * weights)
    
    def match_products(self, database1, database2, threshold=...):
        matches = []
        for product1 in database1:
            best_match = None
            best_score = -float('inf')
            for product2 in database2:
                similarity = self(product1, product2)
                if similarity > best_score:
                    best_score = similarity
                    best_match = product2
            if best_score > threshold:
                matches.append((product1, best_match, best_score))
        
        return matches

def train_embedding_matcher(model, train_data):
    optimizer = torch.optim.Adam(model.parameters())
    criterion = nn.TripletMarginLoss()
    for epoch in range(num_epochs):
        for anchor, positive, negative in train_data:
            anchor_embed = model.product_encoder(anchor)
            positive_embed = model.product_encoder(positive)
            negative_embed = model.product_encoder(negative)
            loss = criterion(anchor_embed, positive_embed, negative_embed)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

class ProductMatchingPipeline:
    def __init__(self, embedding_model):
        self.model = embedding_model
        self.matcher = NCrossEmbeddingMatcher()
    def preprocess_data(self, database):
        processed_database = [
            self.extract_features(product) for product in database
        ]
        return processed_database
    def extract_features(self, product):
        features = [
            product['brand'],
            product['category'],
            ...
        ]
        return features
    
    def match(self, database1, database2):
        processed_db1 = self.preprocess_data(database1)
        processed_db2 = self.preprocess_data(database2)
        matches = self.matcher.match_products(
            processed_db1, 
            processed_db2
        )
        return matches
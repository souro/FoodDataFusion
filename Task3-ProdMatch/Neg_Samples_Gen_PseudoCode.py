def create_negative_examples(dataset):
    def hard_negative(ref_embedding):
        distances = compute_embeddings_distance(ref_embedding)
        hard_negatives = select_challenging_samples(distances)
        return hard_negatives
    
    def soft_negative(ref):
        soft_negatives = [
            add_noise(ref),
            rotate_embedding(ref),
            scale_embedding(ref)
        ]
        return soft_negatives

class NegativeExampleGenerator:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def generate_negatives(self, ref, mode='mixed'):
        if mode == 'hard':
            return self.hard_negative(ref)
        elif mode == 'soft':
            return self.soft_negative(ref)
        else:
            hard_negs = self.hard_negative(ref)
            soft_negs = self.soft_negative(ref)
            return hard_negs + soft_negs

def categorize_negative_samples(ref, negatives):
    difficulty_scores = []
    
    for negative in negatives:
        distance = compute_embedding_distance(ref, negative)
        confidence = model.predict_confidence(negative)
        difficulty_score = compute_difficulty_score(distance, confidence)
        difficulty_scores.append((negative, difficulty_score))
    
    sorted_negatives = sorted(difficulty_scores, key=lambda x: x[1], reverse=True)
    return {
        'hard_negatives': sorted_negatives[:len(sorted_negatives)//2],
        'soft_negatives': sorted_negatives[len(sorted_negatives)//2:]
    }
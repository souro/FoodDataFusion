class ContrastiveLoss(nn.Module):
    def __init__(self, margin=1.0):
        super().__init__()
        self.margin = margin
    def forward(self, anchor, positive, negative):
        pos_distance = torch.pairwise_distance(anchor, positive)
        neg_distance = torch.pairwise_distance(anchor, negative)
        loss = torch.mean(
            torch.max(0, self.margin + pos_distance - neg_distance)
        )
        return loss
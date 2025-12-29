import torch

X = torch.tensor([1., 2., 3., 4.])
y = torch.tensor([3., 5., 7., 9.])

w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

lr = 0.01

for step in range(5):
    # prediction
    y_pred = w * X + b

    # loss
    loss = ((y_pred - y) ** 2).mean()

    # compute gradients
    loss.backward()

    # update parameters (IMPORTANT PART)
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    # reset gradients
    w.grad.zero_()
    b.grad.zero_()

    print(f"Step {step}: w={w.item():.2f}, b={b.item():.2f}, loss={loss.item():.2f}")


#Leaf tensors are trainable parameters.
# PyTorch stores gradients ONLY for leaf tensors.
# Reassigning breaks leaf status.
# In-place updates preserve it.
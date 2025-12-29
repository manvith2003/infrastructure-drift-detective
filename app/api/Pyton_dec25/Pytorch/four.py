import torch

X = torch.tensor([1., 2., 3., 4.])
y = torch.tensor([3., 5., 7., 9.])


w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)


optimizer =torch.optim.SGD([w,b],lr=0.01)

for step in range(20):
    # 1. predict
    y_pred = w * X + b

    # 2. loss
    loss = ((y_pred - y) ** 2).mean()

    # 3. reset gradients
    optimizer.zero_grad()

    # 4. compute gradients
    loss.backward()

    # 5. update parameters
    optimizer.step()

    if step % 5 == 0:
        print(f"Step {step}: w={w.item():.2f}, b={b.item():.2f}, loss={loss.item():.2f}")


print("Final w:", w.item())
print("Final b:", b.item())



# BIG IDEA FIRST (NO CODE)

# Instead of:

# manually changing w and b

# worrying about leaf tensors

# We tell PyTorch:

# “These are my parameters.
# Please update them correctly.”

# That’s what an optimizer does.

# 1️⃣ What Is an Optimizer?

# An optimizer:

# Knows which tensors are trainable

# Updates them using gradients

# Handles all safety rules internally
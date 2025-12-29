import torch

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2

print(y)

y.backward()
print(x.grad)


x1= torch.tensor(2.0, requires_grad=True)

y1 = x1**2
y1.backward()

y2 = x1**3
y2.backward()

print(x1.grad)

#reseting gradient

x.grad.zero_()
print(x.grad)

import torch
import torch.nn as nn

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

print(f"Using {device} device\n")

X = torch.FloatTensor([[0,0],
                        [0,1],
                        [1,0],
                        [1,1]]).to(device)

Y = torch.FloatTensor([[0],[1],[1],[0]]).to(device)

linear = nn.Linear(2, 1)
sigmoid = nn.Sigmoid()
model = nn.Sequential(linear, sigmoid).to(device)
criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
all_epoch=1001
for epoch in range(all_epoch):
	y_pred = model(X)
	loss = criterion(y_pred, Y)

	loss.backward()
	optimizer.step()
	optimizer.zero_grad()

	if epoch%100==0:
		print('Epoch : {}/{}    loss:{}    '.format(epoch, all_epoch, loss.item()))

with torch.no_grad():
	y_hat = (y_pred > 0.5).float()
	accuracy = (y_hat == Y).float().mean()

	print(f'Prediction Value = {y_hat.detach()}    /    Accuracy : {accuracy.item():4f}')

print("="*100)
model_m = nn.Sequential(
	nn.Linear(2,8, True),
	nn.Sigmoid(),
	nn.Linear(8, 16, True),
	nn.Sigmoid(),
	nn.Linear(16, 16 , True),
	nn.Sigmoid(),
	nn.Linear(16, 1, True),
	nn.Sigmoid()
).to(device)

criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.Adam(model_m.parameters(), lr=0.05)
all_epoch=1001
for epoch in range(all_epoch):
	y_pred = model_m(X)
	loss = criterion(y_pred, Y)

	loss.backward()
	optimizer.step()
	optimizer.zero_grad()

	if epoch%100==0:
		print('Epoch : {}/{}    loss:{}    '.format(epoch, all_epoch, loss.item()))

with torch.no_grad():
	y_hat = (y_pred > 0.5).float()
	accuracy = (y_hat == Y).float().mean()

	print(f'Prediction Value = {y_hat.detach()}    /    Accuracy : {accuracy.item():4f}')
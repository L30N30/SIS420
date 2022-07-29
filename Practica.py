import torch
import numpy
from torch.utils.data import TensorDataset, DataLoader
import matplotlib.pyplot as plot
import numpy as np


def run():
    pixels = 28 * 28
    neurons = 32  # 56
    labels = 3

    batch = 1000
    epochs = 250
    lr = 1e-2

    data_train = np.loadtxt('fashion_mnist_tres/fashion-mnist_train.csv', delimiter=',', skiprows=1)
    x_train = data_train[:, 1:pixels+1]/255
    y_train = data_train[:, 0].ravel()
    y_train[(y_train == 10)] = 0

    data_test = np.loadtxt('fashion_mnist_tres/fashion-mnist_test.csv', delimiter=',', skiprows=1)
    x_test = data_test[:, 1:pixels + 1]/255
    y_test = data_test[:, 0].ravel()
    y_test[(y_test == 10)] = 0

    m1 = y_train.size + y_test.size
    porcentaje = round(m1 * 0.7)

    x = np.concatenate([x_train, x_test], axis=0)
    x_train = x[:porcentaje]
    x_test = x[porcentaje:]

    y = np.concatenate([y_train, y_test], axis=0)
    y_train = y[:porcentaje]
    y_test = y[porcentaje:]

    x_t = torch.tensor(x_train, requires_grad=True).float()
    y_t = torch.tensor(y_train, requires_grad=True).long()

    x_t_test = torch.tensor(x_test, requires_grad=True).float()
    y_t_test = torch.tensor(y_test, requires_grad=True).long()

    train_dataset = TensorDataset(x_t, y_t)
    data = DataLoader(train_dataset, batch_size=batch, shuffle=True)

    model = torch.nn.Sequential(
        torch.nn.Linear(pixels, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, labels)
    )

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)  # SGD
    loss = torch.nn.CrossEntropyLoss()

    for epoch in range(epochs):
        l = model(x_t)

        J = loss(l, y_t)
        model.zero_grad()

        J.backward()

        optimizer.step()
        '''for x_b, y_b in data:
            print('batch')
            l = model(x_b)

            J = loss(l, y_b)
            model.zero_grad()

            J.backward()

            optimizer.step()

        print('')'''
        print(f'Epoch {epoch + 1}, Loss: {J.item():.3f}')


run()
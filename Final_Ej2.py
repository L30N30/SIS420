import torch
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
from sklearn.metrics import accuracy_score


def softmax(x):
    return torch.exp(x) / torch.exp(x).sum(axis=-1, keepdims=True)


def evaluate(x, model):
    model.eval()
    y_pred = model(x)
    y_probas = softmax(y_pred)
    return torch.argmax(y_probas, axis=1)


def run():
    pixels = 28 * 28
    neurons = 30
    labels = 5

    epochs = 100
    lr = 1e-2

    data_train = np.loadtxt('MNIST/mnist_train.csv', delimiter=',', skiprows=1)
    x_train = data_train[:, 1:pixels+1]/255
    y_train = data_train[:, 0].ravel()

    data_test = np.loadtxt('MNIST/mnist_test.csv', delimiter=',', skiprows=1)
    x_test = data_test[:, 1:pixels + 1]/255
    y_test = data_test[:, 0].ravel()

    filtro_train = np.where((y_train % 2) == 0)
    x_train = np.delete(x_train, filtro_train, axis=0)
    y_train = np.delete(y_train, filtro_train)

    filtro_test = np.where((y_test % 2) == 0)
    x_test = np.delete(x_test, filtro_test, axis=0)
    y_test = np.delete(y_test, filtro_test)

    m1 = y_train.size + y_test.size
    porcentaje = round(m1 * 0.9)

    x = np.concatenate([x_train, x_test], axis=0)
    x_train = x[:porcentaje]
    x_test = x[porcentaje:]

    y = np.concatenate([y_train, y_test], axis=0)

    y[y == 1] = 0
    y[y == 3] = 1
    y[y == 5] = 2
    y[y == 7] = 3
    y[y == 9] = 4

    y_train = y[:porcentaje]
    y_test = y[porcentaje:]

    x_t = torch.tensor(x_train, requires_grad=True).float()
    y_t = torch.tensor(y_train, requires_grad=True).long()

    model = torch.nn.Sequential(
        torch.nn.Linear(pixels, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, labels)
    )

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    loss = torch.nn.CrossEntropyLoss()

    for epoch in range(epochs):
        l = model(x_t)

        J = loss(l, y_t)
        model.zero_grad()

        J.backward()

        optimizer.step()
        print(f'Epoch {epoch + 1}, Loss: {J.item():.3f}')

    y_predicha = evaluate(torch.from_numpy(x_test).float(), model)
    print(f'Precisión: {round(accuracy_score(y_test, y_predicha.numpy()) * 100, 3)} %')


run()
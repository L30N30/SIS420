import torch
import numpy


def run():
    pixels = 28 * 28
    neurons = 32  # 56
    labels = 10

    batch_size = 100
    epochs = 10000
    lr = 1e-2

    data = numpy.loadtxt('fashion_mnist/fashion-mnist_train.csv', delimiter=',', skiprows=1)
    x = data[:, 1:pixels + 1] / 255
    y = data[:, 0]

    '''data_test = numpy.loadtxt('fashion_mnist/fashion-mnist_test.csv', delimiter=',', skiprows=1)
    x_test = data[:, 1:pixels + 1] / 255
    y_test = data[:, 0]
    x_t_test = torch.tensor(x_test, requires_grad=True).float()
    y_t_test = torch.tensor(y_test, requires_grad=True).long()'''

    x_t = torch.tensor(x, requires_grad=True).float()
    y_t = torch.tensor(y, requires_grad=True).long()

    model = torch.nn.Sequential(
        torch.nn.Linear(pixels, neurons),
        torch.nn.Tanh(),
        torch.nn.Linear(neurons, labels)
        #torch.nn.Tanh(),
        #torch.nn.Linear(neurons, labels)
    )

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    loss = torch.nn.CrossEntropyLoss()

    j_ant = 1000.

    for epoch in range(epochs):
        l = model(x_t)

        J = loss(l, y_t)
        model.zero_grad()

        J.backward()

        optimizer.step()

        print(f'Epoch {epoch + 1}, Loss: {J.item():.3f}')
        if not J.item() < j_ant:
            print('End...')
            break
        else:
            j_ant = J.item() * 1.


run()
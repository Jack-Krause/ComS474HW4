from solution import Net, get_args
from helper import set_random, load_data, train, test


if __name__ == '__main__':
    print("running main")
    exit(0)
    args = get_args()
    set_random(args.seed)
    trainloader, testloader = load_data(args.batch)
    net = Net(args)
    train(net, trainloader, args.num_epochs)
    test(net, testloader)

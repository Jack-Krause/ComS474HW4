from solution import Net, get_args
from helper import set_random, load_data, train, test


if __name__ == '__main__':
    print("running main")
    args = get_args()
    print(f"args:\n{args}")
    set_random(args.seed)
    trainloader, testloader = load_data(args.batch)
    net = Net(args)
    train(net, trainloader, args.num_epochs)
    test(net, testloader)

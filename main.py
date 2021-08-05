import threading

from producer import producer_create
from producer import p_create
from producer import c_create

if __name__ == "__main__":

    var = 1

    while var == 1:

        val = input("Would you like to produce or consume (enter 'p' or 'c'): ")
        if val == "p" or val == "c":
            bootstrap_servers = input("Please input bootstrap servers (ex. localhost:9092): ")
            client_id = input("Please input a client id: ")
            security_protocol = input("Enter the security protocl (ex. PLAIN_SASL: ")
            sasl_mechanism = input("Enter the sasl mechanism (ex. PLAINTEXT)")
            sasl_plain_username = input("Enter a username: ")
            sasl_plain_password = input("Enter a password: ")
            ssl_context = input("Enter an ssl context: ")
            topic = input("Enter a topic name: ")
            producer = producer_create(bootstrap_servers, client_id, security_protocol, sasl_mechanism,
                                    sasl_plain_username, sasl_plain_password, ssl_context);
            if val == "p":
                num_of_messages = input("Enter # of messages wanting to be sent")
                t1 = threading.Thread(p_create(producer, topic, num_of_messages))
                t1.start()
            else:
                t1 = threading.Thread(c_create(topic, bootstrap_servers, client_id, security_protocol, sasl_mechanism,
                                    sasl_plain_username, sasl_plain_password, ssl_context))
                t1.start()
        else:
            print("Incorrect value for producer or consumer")

    #proc1 = mp.Process(target=c_create, args=["c1"])
    #proc1.start()
    #proc1.join()

    #d = {}
    #start_time = time.time()
    #for i in range(1, 2000):
    #    d["proc{0}".format(i)] = mp.Process(target=c_create, args=["c{0}".format(i)])
    #    d["proc{0}".format(i)].start()
    #    print(i)
    #print("--- %s seconds ---" % (time.time() - start_time))
    #t2 = threading.Thread(c_local_create("t2", "test-topic"))
    #t2.start()
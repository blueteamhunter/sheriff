import dns.resolver
import sys, getopt

def resolver_query_a(name, query):
    result = dns.resolver.resolve(name, query)
    for ipval in result:
        result = print("{}".format(ipval.to_text()))
    return result

def resolver_query_all(name, all):
    result = dns.resolver.resolve(name, all)

def main(argv):
    dns_name = ''
    dns_zone = ''
    try:
        opts, args = getopt.getopt(argv, 'd:q:')
    except getopt.GetoptError:
        print ("usage: python sheriff -d <dns_name> -q <dns_zone>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("usage: python sheriff -d <dns_name> -q <dns_zone>")
            sys.exit()
        elif opt in ("-d", "--dns_name"):
            dns_name = arg
        elif opt in ("-q", "--dns_zone"):
            dns_zone = arg

    insert_at_resolver_func = resolver_query_a(dns_name, dns_zone)
    
if __name__ == "__main__":
    main(sys.argv[1:])
    




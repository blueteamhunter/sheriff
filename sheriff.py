import dns.resolver
import sys

def resolver_query_a(name, query):
    try:
        result = dns.resolver.resolve(name, query)
        pass
        for ipval in result:
            result = print("{} Record Lookup : {}".format(query,ipval.to_text()))
        return result
    except:
        print("{} Record Lookup not found".format(query))
        pass

def main(argv):
    if len (sys.argv) != 2:
        print("Usage: python example.com")
        sys.exit(1)
    dns_name = str(sys.argv[1])
    dns_zone = ""
    dns_all_zones = ["A", "MX", "NS", "SOA", "TXT"]

    for item in dns_all_zones:
        dns_zone = item
        resolver_query_a(dns_name, dns_zone)

if __name__ == "__main__":
    main(sys.argv[1:])
    




import dns.resolver
import dns.zone
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
    
def dns_zone_transfer(address):
    print ("\n[*] Atempting zone transfer [*]\n")
    dns_ns_awnswer = dns.resolver.resolve(address, 'NS')
    for server in dns_ns_awnswer:
        dns_ns_awnswer = dns.resolver.resolve(address, 'A')
        for ip in dns_ns_awnswer:
            try:
                zone = dns.zone.from_xrf(dns.query.xfr(str(ip), address))
                for host in zone:
                    print("[*] Possible zone transfer found: {}".format(host))
            except Exception as e:
                print("[*] NS {} is refusing zone transfer!".format(server))
                continue

def main(argv):
    if len (sys.argv) != 2:
        print("Usage: python example.com")
        sys.exit(1)
    dns_name = str(sys.argv[1])
    dns_name = "google.com"
    dns_zone = ""
    dns_all_zones = ["A", "MX", "NS", "SOA", "TXT"]

    for item in dns_all_zones:
        dns_zone = item
        resolver_query_a(dns_name, dns_zone)
        
    dns_zone_transfer(dns_name)

if __name__ == "__main__":
    main(sys.argv[1:])
    





# this program used to find the ingredlent adjuster

cookies = 48
sugre = 1.5
flour = 2.75e
butter = 1

numberOfCookie = int(input("enter the nunber of cookies youb want to make ".title() ))


# this to calculate the sugre need for making the cookies
sugreNeed = (sugre * numberOfCookie) / cookies

flourNeed = (flour * numberOfCookie) / cookies

butterNeed = (butter * numberOfCookie) / cookies

print(f"\n\nthe amount of cookies he or she wanks to makes is \
      numberOfCookie:.2f}\nthe amiunt of sugre need is {sugreNeed:.2f}\nthe \
      amount of flour need is {flourNeed:.2f}\nthe amount of butter need is \
      {butterNeed:.2f}".title())

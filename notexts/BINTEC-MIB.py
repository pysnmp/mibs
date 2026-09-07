#
# PySNMP MIB module BINTEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source BINTEC-MIB
# Source digest sha256:798a439ac05071350cf730815b54bd2a18eb0d47c3eafab21314a76909efb281
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
isdn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 2))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
atm = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 16))
sys = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17))
admin_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 22)).setLabel("admin-2")
vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 23))
ipsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 26))
qos = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 27))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 30))
voip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 33))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 38))
vif = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 39))
tty = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 41))
ssh = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 44))
phy = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 45))
wlan = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 46))
ima = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 54))
usb = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 55))
resource = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17, 4))
gui = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 69))
class PhysAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Date(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class HexValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class BitValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("BINTEC-MIB", BitValue=BitValue, BridgeId=BridgeId, Date=Date, DisplayString=DisplayString, HexValue=HexValue, MacAddress=MacAddress, PhysAddress=PhysAddress, Timeout=Timeout, admin_2=admin_2, adsl=adsl, atm=atm, bibo=bibo, biboip=biboip, bintec=bintec, gui=gui, ima=ima, ipsec=ipsec, isdn=isdn, phy=phy, qos=qos, resource=resource, security=security, ssh=ssh, sys=sys, tty=tty, usb=usb, vif=vif, voip=voip, vpn=vpn, wlan=wlan)

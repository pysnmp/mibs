#
# PySNMP MIB module IB-DNSSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source IB-DNSSERV-MIB
# Source digest sha256:f08e5103c82f6d93b2419d2220d579a6847a71be160d7ba81ff6fa908d73190f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
IbString, ibDNSServ = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "ibDNSServ")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibDnsServMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 32, 1))
ibDnsServMIBModule.setRevisions(('2011-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibDnsServMIBModule.setRevisionsDescriptions(('Creation of the DNS Server MIB file',))
if mibBuilder.loadTexts: ibDnsServMIBModule.setLastUpdated('2011-07-13 00:00')
if mibBuilder.loadTexts: ibDnsServMIBModule.setOrganization('Infoblox')
if mibBuilder.loadTexts: ibDnsServMIBModule.setContactInfo('Please See IB-SMI-MIB.')
if mibBuilder.loadTexts: ibDnsServMIBModule.setDescription('This file defines the Infoblox DNS Server MIB.')
ibDnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1))
ibDnsServConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1, 1))
ibDnsServConfigImplementIdent = MibScalar((1, 3, 6, 1, 4, 1, 32, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setStatus('current')
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setDescription('The implementation identification string for\n                  the DNS server software in use on the system.')
mibBuilder.exportSymbols("IB-DNSSERV-MIB", PYSNMP_MODULE_ID=ibDnsServMIBModule, ibDnsServConfig=ibDnsServConfig, ibDnsServConfigImplementIdent=ibDnsServConfigImplementIdent, ibDnsServMIBModule=ibDnsServMIBModule, ibDnsServMIBObjects=ibDnsServMIBObjects)

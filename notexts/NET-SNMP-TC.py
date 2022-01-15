#
# PySNMP MIB module NET-SNMP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-TC
# Produced by pysmi-1.1.8 at Sat Jan 15 19:49:04 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
netSnmpAgentOIDs, netSnmpModuleIDs, netSnmpDomains = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpAgentOIDs", "netSnmpModuleIDs", "netSnmpDomains")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ObjectIdentity, Opaque, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Integer32, Counter32, Counter64, Gauge32, TimeTicks, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ObjectIdentity", "Opaque", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "Gauge32", "TimeTicks", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpTCs = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 1))
netSnmpTCs.setRevisions(('2002-02-12 00:00',))
if mibBuilder.loadTexts: netSnmpTCs.setLastUpdated('200510140000Z')
if mibBuilder.loadTexts: netSnmpTCs.setOrganization('www.net-snmp.org')
class Float(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

hpux9 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 1))
sunos4 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 2))
solaris = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 3))
osf = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 4))
ultrix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 5))
hpux10 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 6))
netbsd = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 7))
freebsd = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 8))
irix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 9))
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 10))
bsdi = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 11))
openbsd = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 12))
win32 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 13))
hpux11 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 14))
aix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 15))
macosx = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 16))
dragonfly = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 17))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 255))
netSnmpTCPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 1))
netSnmpUnixDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 2))
netSnmpAAL5PVCDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 3))
netSnmpUDPIPv6Domain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 4))
netSnmpTCPIPv6Domain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 5))
netSnmpCallbackDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 6))
netSnmpAliasDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 7))
netSnmpDTLSUDPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 8))
netSnmpDTLSSCTPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 9))
netSnmpTLSTCPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 10))
mibBuilder.exportSymbols("NET-SNMP-TC", openbsd=openbsd, netSnmpTCPDomain=netSnmpTCPDomain, netSnmpAAL5PVCDomain=netSnmpAAL5PVCDomain, irix=irix, netSnmpAliasDomain=netSnmpAliasDomain, solaris=solaris, Float=Float, netSnmpDTLSUDPDomain=netSnmpDTLSUDPDomain, sunos4=sunos4, hpux9=hpux9, netSnmpTCPIPv6Domain=netSnmpTCPIPv6Domain, netSnmpUnixDomain=netSnmpUnixDomain, netSnmpTCs=netSnmpTCs, netSnmpTLSTCPDomain=netSnmpTLSTCPDomain, dragonfly=dragonfly, macosx=macosx, bsdi=bsdi, netSnmpDTLSSCTPDomain=netSnmpDTLSSCTPDomain, linux=linux, PYSNMP_MODULE_ID=netSnmpTCs, freebsd=freebsd, osf=osf, netSnmpCallbackDomain=netSnmpCallbackDomain, win32=win32, ultrix=ultrix, unknown=unknown, hpux11=hpux11, aix=aix, netbsd=netbsd, netSnmpUDPIPv6Domain=netSnmpUDPIPv6Domain, hpux10=hpux10)

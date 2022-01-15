#
# PySNMP MIB module NET-SNMP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-TC
# Produced by pysmi-1.1.8 at Sat Jan 15 16:47:43 2022
# On host fv-az126-328 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
netSnmpDomains, netSnmpAgentOIDs, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpDomains", "netSnmpAgentOIDs", "netSnmpModuleIDs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Opaque, iso, MibIdentifier, Integer32, Gauge32, Counter64, NotificationType, Unsigned32, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Opaque", "iso", "MibIdentifier", "Integer32", "Gauge32", "Counter64", "NotificationType", "Unsigned32", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NET-SNMP-TC", netSnmpUnixDomain=netSnmpUnixDomain, netSnmpTCs=netSnmpTCs, netSnmpCallbackDomain=netSnmpCallbackDomain, hpux10=hpux10, linux=linux, netSnmpAAL5PVCDomain=netSnmpAAL5PVCDomain, netSnmpDTLSSCTPDomain=netSnmpDTLSSCTPDomain, hpux11=hpux11, netSnmpDTLSUDPDomain=netSnmpDTLSUDPDomain, netSnmpTCPIPv6Domain=netSnmpTCPIPv6Domain, PYSNMP_MODULE_ID=netSnmpTCs, solaris=solaris, unknown=unknown, openbsd=openbsd, netSnmpAliasDomain=netSnmpAliasDomain, osf=osf, netSnmpTLSTCPDomain=netSnmpTLSTCPDomain, win32=win32, dragonfly=dragonfly, Float=Float, netbsd=netbsd, freebsd=freebsd, bsdi=bsdi, hpux9=hpux9, macosx=macosx, sunos4=sunos4, irix=irix, netSnmpTCPDomain=netSnmpTCPDomain, netSnmpUDPIPv6Domain=netSnmpUDPIPv6Domain, ultrix=ultrix, aix=aix)

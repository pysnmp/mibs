#
# PySNMP MIB module ENTERASYS-MIB-NAMES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/ENTERASYS-MIB-NAMES
# Produced by pysmi-1.1.12 at Tue Sep 17 12:21:55 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Counter32, Unsigned32, Integer32, MibIdentifier, enterprises, ModuleIdentity, iso, ObjectIdentity, NotificationType, TimeTicks, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Counter32", "Unsigned32", "Integer32", "MibIdentifier", "enterprises", "ModuleIdentity", "iso", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysModuleName = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 1))
etsysModuleName.setRevisions(('2003-11-06 15:15', '2003-10-23 17:19', '2002-06-14 16:02', '2002-06-14 14:02', '2000-11-13 21:21', '2000-10-05 13:00', '2000-04-07 00:00', '2000-03-21 00:00',))
if mibBuilder.loadTexts: etsysModuleName.setLastUpdated('200311061515Z')
if mibBuilder.loadTexts: etsysModuleName.setOrganization('Enterasys Networks, Inc')
enterasys = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624))
if mibBuilder.loadTexts: enterasys.setStatus('current')
etsysMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1))
etsysOids = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 2))
etsysAgentCaps = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 3))
etsysX509Pki = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 509))
etsysModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2))
etsysNamesMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 1))
if mibBuilder.loadTexts: etsysNamesMib.setStatus('obsolete')
etsysConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 3))
if mibBuilder.loadTexts: etsysConformance.setStatus('obsolete')
etsysConformName = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 3, 1))
if mibBuilder.loadTexts: etsysConformName.setStatus('obsolete')
etsysConformOID = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 3, 2))
if mibBuilder.loadTexts: etsysConformOID.setStatus('obsolete')
mibBuilder.exportSymbols("ENTERASYS-MIB-NAMES", etsysConformName=etsysConformName, etsysOids=etsysOids, etsysNamesMib=etsysNamesMib, etsysMibs=etsysMibs, enterasys=enterasys, etsysModuleName=etsysModuleName, etsysAgentCaps=etsysAgentCaps, etsysModules=etsysModules, etsysConformance=etsysConformance, PYSNMP_MODULE_ID=etsysModuleName, etsysX509Pki=etsysX509Pki, etsysConformOID=etsysConformOID)

#
# PySNMP MIB module ENTERASYS-MIB-NAMES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/ENTERASYS-MIB-NAMES
# Produced by pysmi-1.1.8 at Thu Sep 29 13:09:19 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, iso, Integer32, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "Integer32", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "Bits", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-MIB-NAMES", etsysModuleName=etsysModuleName, etsysConformName=etsysConformName, PYSNMP_MODULE_ID=etsysModuleName, etsysX509Pki=etsysX509Pki, etsysModules=etsysModules, etsysNamesMib=etsysNamesMib, etsysAgentCaps=etsysAgentCaps, etsysConformOID=etsysConformOID, etsysMibs=etsysMibs, etsysConformance=etsysConformance, etsysOids=etsysOids, enterasys=enterasys)

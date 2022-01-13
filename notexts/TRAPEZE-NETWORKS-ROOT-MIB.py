#
# PySNMP MIB module TRAPEZE-NETWORKS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/TRAPEZE-NETWORKS-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:06:17 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Unsigned32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, TimeTicks, Integer32, Gauge32, ModuleIdentity, NotificationType, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "TimeTicks", "Integer32", "Gauge32", "ModuleIdentity", "NotificationType", "MibIdentifier", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525))
trpzRootMib.setRevisions(('2008-05-22 00:08', '2007-11-28 00:07', '2006-04-14 00:06', '2005-01-01 00:00',))
if mibBuilder.loadTexts: trpzRootMib.setLastUpdated('200805220008Z')
if mibBuilder.loadTexts: trpzRootMib.setOrganization('Trapeze Networks')
trpzProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 1))
trpzTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 2))
trpzRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3))
trpzMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4))
trpzTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 5))
trpzMgmtAppMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 6))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-ROOT-MIB", trpzRootMib=trpzRootMib, trpzProducts=trpzProducts, trpzMibs=trpzMibs, trpzMgmtAppMibs=trpzMgmtAppMibs, trpzTemporary=trpzTemporary, trpzRegistration=trpzRegistration, trpzTraps=trpzTraps, PYSNMP_MODULE_ID=trpzRootMib)

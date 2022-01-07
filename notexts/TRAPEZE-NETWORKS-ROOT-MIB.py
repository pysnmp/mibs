#
# PySNMP MIB module TRAPEZE-NETWORKS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/TRAPEZE-NETWORKS-ROOT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:21 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Bits, Counter64, IpAddress, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Bits", "Counter64", "IpAddress", "enterprises", "ObjectIdentity")
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
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-ROOT-MIB", trpzRegistration=trpzRegistration, trpzMibs=trpzMibs, trpzProducts=trpzProducts, trpzTraps=trpzTraps, trpzRootMib=trpzRootMib, trpzTemporary=trpzTemporary, trpzMgmtAppMibs=trpzMgmtAppMibs, PYSNMP_MODULE_ID=trpzRootMib)

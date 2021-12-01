#
# PySNMP MIB module TRAPEZE-NETWORKS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/TRAPEZE-NETWORKS-ROOT-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:14:24 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, Gauge32, Unsigned32, MibIdentifier, enterprises, iso, Counter64, ModuleIdentity, IpAddress, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "enterprises", "iso", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-ROOT-MIB", trpzRegistration=trpzRegistration, trpzMgmtAppMibs=trpzMgmtAppMibs, trpzTraps=trpzTraps, trpzRootMib=trpzRootMib, trpzProducts=trpzProducts, PYSNMP_MODULE_ID=trpzRootMib, trpzTemporary=trpzTemporary, trpzMibs=trpzMibs)

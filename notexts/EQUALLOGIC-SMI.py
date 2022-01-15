#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Sat Jan 15 17:14:30 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, enterprises, NotificationType, Integer32, iso, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, IpAddress, Counter64, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "iso", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "IpAddress", "Counter64", "ObjectIdentity", "Unsigned32")
TruthValue, RowPointer, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowPointer", "RowStatus", "TextualConvention", "DisplayString")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", eqlPSSeries=eqlPSSeries, equalLogic=equalLogic, PYSNMP_MODULE_ID=equalLogic, products=products)

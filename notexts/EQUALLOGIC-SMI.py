#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Sat Jan 15 04:40:32 2022
# On host fv-az83-73 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, IpAddress, Integer32, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, MibIdentifier, TimeTicks, iso, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "IpAddress", "Integer32", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "MibIdentifier", "TimeTicks", "iso", "Counter64", "ModuleIdentity", "Unsigned32")
RowStatus, RowPointer, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "RowPointer", "TruthValue", "TextualConvention", "DisplayString")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, equalLogic=equalLogic, PYSNMP_MODULE_ID=equalLogic, eqlPSSeries=eqlPSSeries)

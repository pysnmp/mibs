#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Mon Jul  1 09:12:36 2024
# On host fv-az532-988 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, iso, enterprises, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, Bits, TimeTicks, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "iso", "enterprises", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "Bits", "TimeTicks", "Counter32", "Counter64")
TruthValue, DisplayString, RowPointer, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowPointer", "RowStatus", "TextualConvention")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", equalLogic=equalLogic, PYSNMP_MODULE_ID=equalLogic, products=products, eqlPSSeries=eqlPSSeries)

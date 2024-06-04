#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Tue Jun  4 08:18:06 2024
# On host fv-az530-683 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, Counter64, Bits, Unsigned32, ModuleIdentity, Gauge32, NotificationType, MibIdentifier, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "Counter64", "Bits", "Unsigned32", "ModuleIdentity", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "TimeTicks")
TruthValue, RowStatus, DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "RowPointer", "TextualConvention")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, eqlPSSeries=eqlPSSeries, equalLogic=equalLogic, PYSNMP_MODULE_ID=equalLogic)

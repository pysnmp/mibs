#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Mon Jun  3 12:22:46 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, Counter64, iso, Integer32, Gauge32, Counter32, TimeTicks, ModuleIdentity, enterprises, MibIdentifier, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "iso", "Integer32", "Gauge32", "Counter32", "TimeTicks", "ModuleIdentity", "enterprises", "MibIdentifier", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
RowPointer, DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", eqlPSSeries=eqlPSSeries, products=products, PYSNMP_MODULE_ID=equalLogic, equalLogic=equalLogic)

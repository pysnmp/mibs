#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Tue Jan 18 14:05:20 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, IpAddress, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ObjectIdentity, enterprises, MibIdentifier, Unsigned32, Bits, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ObjectIdentity", "enterprises", "MibIdentifier", "Unsigned32", "Bits", "Integer32", "NotificationType")
RowPointer, DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", equalLogic=equalLogic, products=products, PYSNMP_MODULE_ID=equalLogic, eqlPSSeries=eqlPSSeries)

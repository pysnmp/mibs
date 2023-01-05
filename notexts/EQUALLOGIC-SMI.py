#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Thu Jan  5 09:23:18 2023
# On host fv-az581-610 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, enterprises, NotificationType, Counter32, IpAddress, iso, Bits, ObjectIdentity, Integer32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "enterprises", "NotificationType", "Counter32", "IpAddress", "iso", "Bits", "ObjectIdentity", "Integer32", "MibIdentifier", "TimeTicks")
TruthValue, RowPointer, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowPointer", "DisplayString", "RowStatus", "TextualConvention")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, eqlPSSeries=eqlPSSeries, PYSNMP_MODULE_ID=equalLogic, equalLogic=equalLogic)

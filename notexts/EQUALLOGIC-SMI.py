#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Wed May 29 08:09:50 2024
# On host fv-az698-992 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Bits, Counter32, Counter64, enterprises, Gauge32, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Bits", "Counter32", "Counter64", "enterprises", "Gauge32", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "ModuleIdentity", "TimeTicks")
RowStatus, TruthValue, DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "RowPointer", "TextualConvention")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", equalLogic=equalLogic, products=products, PYSNMP_MODULE_ID=equalLogic, eqlPSSeries=eqlPSSeries)

#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:31 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, IpAddress, Bits, Counter64, Counter32, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "IpAddress", "Bits", "Counter64", "Counter32", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType", "iso", "TimeTicks", "ModuleIdentity")
RowPointer, TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", PYSNMP_MODULE_ID=equalLogic, equalLogic=equalLogic, eqlPSSeries=eqlPSSeries, products=products)

#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Tue Sep 17 12:56:48 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, Unsigned32, Counter32, MibIdentifier, iso, Counter64, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "iso", "Counter64", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "IpAddress")
TextualConvention, DisplayString, TruthValue, RowStatus, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus", "RowPointer")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", PYSNMP_MODULE_ID=equalLogic, products=products, eqlPSSeries=eqlPSSeries, equalLogic=equalLogic)

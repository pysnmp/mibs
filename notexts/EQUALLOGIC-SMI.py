#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Tue May 28 13:58:09 2024
# On host fv-az529-55 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, iso, Bits, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, NotificationType, Counter32, enterprises, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "iso", "Bits", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "NotificationType", "Counter32", "enterprises", "Counter64", "TimeTicks")
DisplayString, RowStatus, TextualConvention, TruthValue, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "RowPointer")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", PYSNMP_MODULE_ID=equalLogic, equalLogic=equalLogic, eqlPSSeries=eqlPSSeries, products=products)

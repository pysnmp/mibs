#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.12 at Mon Jun  3 13:07:48 2024
# On host fv-az1121-719 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, enterprises, TimeTicks, Counter32, Bits, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Unsigned32, Counter64, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "enterprises", "TimeTicks", "Counter32", "Bits", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Unsigned32", "Counter64", "MibIdentifier", "ObjectIdentity")
RowStatus, RowPointer, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "RowPointer", "TextualConvention", "DisplayString", "TruthValue")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, equalLogic=equalLogic, PYSNMP_MODULE_ID=equalLogic, eqlPSSeries=eqlPSSeries)

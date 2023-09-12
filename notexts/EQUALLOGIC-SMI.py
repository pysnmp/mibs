#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Tue Sep 12 09:38:25 2023
# On host fv-az502-117 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64, Gauge32, enterprises, NotificationType, TimeTicks, Counter32, Integer32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64", "Gauge32", "enterprises", "NotificationType", "TimeTicks", "Counter32", "Integer32", "IpAddress", "Bits")
DisplayString, TruthValue, RowPointer, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowPointer", "RowStatus", "TextualConvention")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, eqlPSSeries=eqlPSSeries, equalLogic=equalLogic, PYSNMP_MODULE_ID=equalLogic)

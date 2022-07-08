#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Fri Jul  8 08:21:29 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Counter32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Counter64, ObjectIdentity, MibIdentifier, NotificationType, Gauge32, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Counter32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType", "Gauge32", "enterprises", "Unsigned32")
TextualConvention, RowPointer, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "RowStatus", "DisplayString", "TruthValue")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, equalLogic=equalLogic, eqlPSSeries=eqlPSSeries, PYSNMP_MODULE_ID=equalLogic)

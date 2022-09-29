#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQUALLOGIC-SMI
# Produced by pysmi-1.1.8 at Thu Sep 29 13:09:21 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, NotificationType, TimeTicks, Gauge32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, MibIdentifier, Counter32, IpAddress, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter32", "IpAddress", "enterprises", "Integer32")
TextualConvention, RowStatus, TruthValue, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "RowPointer", "DisplayString")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", eqlPSSeries=eqlPSSeries, PYSNMP_MODULE_ID=equalLogic, equalLogic=equalLogic, products=products)

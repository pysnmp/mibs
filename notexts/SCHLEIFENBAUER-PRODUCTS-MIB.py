#
# PySNMP MIB module SCHLEIFENBAUER-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-PRODUCTS-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:35:53 2021
# On host fv-az135-680 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
schleifenbauerModules, schleifenbauerProducts = mibBuilder.importSymbols("SCHLEIFENBAUER-SMI", "schleifenbauerModules", "schleifenbauerProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, iso, Counter32, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "iso", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
schleifenbauerProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034, 13, 2))
schleifenbauerProductsMIB.setRevisions(('2015-10-23 00:00',))
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setOrganization('Schleifenbauer Engineering')
hpdu = MibIdentifier((1, 3, 6, 1, 4, 1, 31034, 11, 1))
dpm3 = MibIdentifier((1, 3, 6, 1, 4, 1, 31034, 11, 2))
mibBuilder.exportSymbols("SCHLEIFENBAUER-PRODUCTS-MIB", hpdu=hpdu, PYSNMP_MODULE_ID=schleifenbauerProductsMIB, schleifenbauerProductsMIB=schleifenbauerProductsMIB, dpm3=dpm3)

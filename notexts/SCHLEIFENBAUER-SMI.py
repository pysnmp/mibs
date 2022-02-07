#
# PySNMP MIB module SCHLEIFENBAUER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-SMI
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:20 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, IpAddress, Bits, Counter32, Unsigned32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, TimeTicks, NotificationType, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "Bits", "Counter32", "Unsigned32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "TimeTicks", "NotificationType", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
schleifenbauer = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034))
schleifenbauer.setRevisions(('2015-10-23 00:00',))
if mibBuilder.loadTexts: schleifenbauer.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauer.setOrganization('Schleifenbauer Engineering')
schleifenbauerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 11))
if mibBuilder.loadTexts: schleifenbauerProducts.setStatus('current')
schleifenbauerMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 12))
if mibBuilder.loadTexts: schleifenbauerMgmt.setStatus('current')
schleifenbauerModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 13))
if mibBuilder.loadTexts: schleifenbauerModules.setStatus('current')
mibBuilder.exportSymbols("SCHLEIFENBAUER-SMI", schleifenbauerProducts=schleifenbauerProducts, schleifenbauerModules=schleifenbauerModules, schleifenbauer=schleifenbauer, schleifenbauerMgmt=schleifenbauerMgmt, PYSNMP_MODULE_ID=schleifenbauer)

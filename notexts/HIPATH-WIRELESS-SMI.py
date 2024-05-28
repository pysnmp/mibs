#
# PySNMP MIB module HIPATH-WIRELESS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ewc/HIPATH-WIRELESS-SMI
# Produced by pysmi-1.1.12 at Tue May 28 12:48:24 2024
# On host fv-az847-244 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, ModuleIdentity, NotificationType, ObjectIdentity, IpAddress, Counter32, TimeTicks, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "ModuleIdentity", "NotificationType", "ObjectIdentity", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hiPathWireless = ModuleIdentity((1, 3, 6, 1, 4, 1, 4329, 15))
hiPathWireless.setRevisions(('2005-07-21 02:37',))
if mibBuilder.loadTexts: hiPathWireless.setLastUpdated('200507210237Z')
if mibBuilder.loadTexts: hiPathWireless.setOrganization('Chantry Networks, Inc.')
siemens = MibIdentifier((1, 3, 6, 1, 4, 1, 4329))
hiPathWirelessProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1))
if mibBuilder.loadTexts: hiPathWirelessProducts.setStatus('current')
hiPathWirelessMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 3))
if mibBuilder.loadTexts: hiPathWirelessMgmt.setStatus('current')
hiPathWirelessDevelopment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 4))
if mibBuilder.loadTexts: hiPathWirelessDevelopment.setStatus('current')
hiPathWirelessModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 5))
if mibBuilder.loadTexts: hiPathWirelessModules.setStatus('current')
hiPathWirelessHWM = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 6))
if mibBuilder.loadTexts: hiPathWirelessHWM.setStatus('current')
mibBuilder.exportSymbols("HIPATH-WIRELESS-SMI", siemens=siemens, hiPathWirelessMgmt=hiPathWirelessMgmt, hiPathWirelessDevelopment=hiPathWirelessDevelopment, hiPathWirelessHWM=hiPathWirelessHWM, PYSNMP_MODULE_ID=hiPathWireless, hiPathWireless=hiPathWireless, hiPathWirelessModules=hiPathWirelessModules, hiPathWirelessProducts=hiPathWirelessProducts)

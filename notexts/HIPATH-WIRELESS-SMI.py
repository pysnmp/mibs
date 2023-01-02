#
# PySNMP MIB module HIPATH-WIRELESS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ewc/HIPATH-WIRELESS-SMI
# Produced by pysmi-1.1.8 at Mon Jan  2 15:28:41 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, Gauge32, ObjectIdentity, Counter32, NotificationType, Integer32, Bits, Counter64, ModuleIdentity, Unsigned32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "Gauge32", "ObjectIdentity", "Counter32", "NotificationType", "Integer32", "Bits", "Counter64", "ModuleIdentity", "Unsigned32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HIPATH-WIRELESS-SMI", siemens=siemens, hiPathWirelessProducts=hiPathWirelessProducts, hiPathWirelessDevelopment=hiPathWirelessDevelopment, hiPathWirelessHWM=hiPathWirelessHWM, hiPathWirelessModules=hiPathWirelessModules, hiPathWirelessMgmt=hiPathWirelessMgmt, hiPathWireless=hiPathWireless, PYSNMP_MODULE_ID=hiPathWireless)

#
# PySNMP MIB module ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:51:40 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, NotificationType, Counter32, Unsigned32, Bits, Integer32, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "Bits", "Integer32", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSOverTempProtectionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 10))
adGenAOSOverTempProtectionMib.setRevisions(('2014-11-04 16:15',))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setLastUpdated('201411041615Z')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setOrganization('ADTRAN, Inc.')
adGenAOSOverTempProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10))
adGenAOSOverTempProtectionTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0))
adGenAOSOverTempProtectionWarning = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 1))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionWarning.setStatus('current')
adGenAOSOverTempProtectionShutdown = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 2))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionShutdown.setStatus('current')
adGenAOSOverTempProtectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19))
adGenAOSOverTempProtectionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1))
adGenAOSOverTempProtectionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2))
adGenAOSOverTempProtectionFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionFullCompliance = adGenAOSOverTempProtectionFullCompliance.setStatus('current')
adGenAOSOverTempProtectionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionWarning"), ("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionNotificationGroup = adGenAOSOverTempProtectionNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", adGenAOSOverTempProtectionTrap=adGenAOSOverTempProtectionTrap, adGenAOSOverTempProtectionFullCompliance=adGenAOSOverTempProtectionFullCompliance, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSOverTempProtectionWarning=adGenAOSOverTempProtectionWarning, PYSNMP_MODULE_ID=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionNotificationGroup=adGenAOSOverTempProtectionNotificationGroup, adGenAOSOverTempProtectionShutdown=adGenAOSOverTempProtectionShutdown, adGenAOSOverTempProtectionCompliances=adGenAOSOverTempProtectionCompliances, adGenAOSOverTempProtectionGroups=adGenAOSOverTempProtectionGroups, adGenAOSOverTempProtectionMib=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionConformance=adGenAOSOverTempProtectionConformance)

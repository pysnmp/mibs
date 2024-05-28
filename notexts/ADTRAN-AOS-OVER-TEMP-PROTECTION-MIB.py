#
# PySNMP MIB module ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:44:42 2024
# On host fv-az847-244 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Unsigned32, MibIdentifier, iso, Counter32, IpAddress, ModuleIdentity, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Unsigned32", "MibIdentifier", "iso", "Counter32", "IpAddress", "ModuleIdentity", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", adGenAOSOverTempProtectionShutdown=adGenAOSOverTempProtectionShutdown, adGenAOSOverTempProtectionCompliances=adGenAOSOverTempProtectionCompliances, adGenAOSOverTempProtectionWarning=adGenAOSOverTempProtectionWarning, PYSNMP_MODULE_ID=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionFullCompliance=adGenAOSOverTempProtectionFullCompliance, adGenAOSOverTempProtectionConformance=adGenAOSOverTempProtectionConformance, adGenAOSOverTempProtectionNotificationGroup=adGenAOSOverTempProtectionNotificationGroup, adGenAOSOverTempProtectionTrap=adGenAOSOverTempProtectionTrap, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSOverTempProtectionMib=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionGroups=adGenAOSOverTempProtectionGroups)

#
# PySNMP MIB module ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 10:50:40 2024
# On host fv-az665-510 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, NotificationType, ModuleIdentity, Gauge32, TimeTicks, Counter32, IpAddress, MibIdentifier, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Gauge32", "TimeTicks", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSOverTempProtectionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 10))
adGenAOSOverTempProtectionMib.setRevisions(('2014-11-04 16:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setRevisionsDescriptions(('Created the adGenAosOverTempProtection MIB. Revision R11.6',))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setLastUpdated('201411041615Z')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setContactInfo('        Technical Support Dept.\n            \t\tPostal: ADTRAN, Inc.\n                    901 Explorer Blvd.\n                    Huntsville, AL 35806\n\n               Tel: +1 800 726-8663\n               Fax: +1 256 963 6217\n            E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setDescription('The MIB module defines over-temperature configuration information and traps for AdtranOS products.')
adGenAOSOverTempProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10))
adGenAOSOverTempProtectionTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0))
adGenAOSOverTempProtectionWarning = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 1))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionWarning.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionWarning.setDescription('An over-temperature warning trap signifies that the warning temperature threshold has been exceeded.')
adGenAOSOverTempProtectionShutdown = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 2))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionShutdown.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionShutdown.setDescription('An over-temperature shutdown trap signifies that the shutdown temperature threshold has been exceeded, and the unit will restart into low-power mode.')
adGenAOSOverTempProtectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19))
adGenAOSOverTempProtectionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1))
adGenAOSOverTempProtectionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2))
adGenAOSOverTempProtectionFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionFullCompliance = adGenAOSOverTempProtectionFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        version 2 of the adGenAosOverTempProtection MIB. When the implementation of this MIB \n        supports adGenAOSOverTempProtectionNotificationGroup, then such an implementation can claim\n        full compliance.')
adGenAOSOverTempProtectionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionWarning"), ("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionNotificationGroup = adGenAOSOverTempProtectionNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionNotificationGroup.setDescription("Traps which may be used to enhance event driven\n            management of the chassis's over-temperature protection subsystem.")
mibBuilder.exportSymbols("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", adGenAOSOverTempProtectionCompliances=adGenAOSOverTempProtectionCompliances, adGenAOSOverTempProtectionShutdown=adGenAOSOverTempProtectionShutdown, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSOverTempProtectionWarning=adGenAOSOverTempProtectionWarning, adGenAOSOverTempProtectionNotificationGroup=adGenAOSOverTempProtectionNotificationGroup, adGenAOSOverTempProtectionConformance=adGenAOSOverTempProtectionConformance, adGenAOSOverTempProtectionFullCompliance=adGenAOSOverTempProtectionFullCompliance, adGenAOSOverTempProtectionMib=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionTrap=adGenAOSOverTempProtectionTrap, PYSNMP_MODULE_ID=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionGroups=adGenAOSOverTempProtectionGroups)

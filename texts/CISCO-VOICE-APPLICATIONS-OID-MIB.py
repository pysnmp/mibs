#
# PySNMP MIB module CISCO-VOICE-APPLICATIONS-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-APPLICATIONS-OID-MIB
# Source digest sha256:a3224fbd7a68348f62d01bcc9f18d2623246cff9b2c7d17dd10e6d60a1f0e8e4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceApplicationsOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 5))
ciscoVoiceApplicationsOIDMIB.setRevisions(('2004-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setLastUpdated('2004-06-17 00:00')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-itm@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setDescription('This module defines the object identifiers that are\n            assigned to various Cisco voice applications. Voice\n            applications include call agents and other voice \n            application products. Call agents are call processing\n            components of a device in a IP telephony and VoIP network.')
cvaMIBOids = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1))
ciscoCallManager = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 1))
ciscoCallManagerExpress = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 2))
ciscoSRST = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 3))
ciscoBTS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 4))
ciscoCSPS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 5))
mibBuilder.exportSymbols("CISCO-VOICE-APPLICATIONS-OID-MIB", PYSNMP_MODULE_ID=ciscoVoiceApplicationsOIDMIB, ciscoBTS=ciscoBTS, ciscoCSPS=ciscoCSPS, ciscoCallManager=ciscoCallManager, ciscoCallManagerExpress=ciscoCallManagerExpress, ciscoSRST=ciscoSRST, ciscoVoiceApplicationsOIDMIB=ciscoVoiceApplicationsOIDMIB, cvaMIBOids=cvaMIBOids)

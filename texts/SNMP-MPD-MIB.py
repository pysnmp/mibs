#
# PySNMP MIB module SNMP-MPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-MPD-MIB
# Produced by pysmi-1.1.3 at Thu Dec  9 14:28:56 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Gauge32, Unsigned32, Counter32, MibIdentifier, Counter64, Bits, Integer32, ObjectIdentity, snmpModules, ModuleIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Gauge32", "Unsigned32", "Counter32", "MibIdentifier", "Counter64", "Bits", "Integer32", "ObjectIdentity", "snmpModules", "ModuleIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpMPDMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 11))
snmpMPDMIB.setRevisions(('2002-10-14 00:00', '1999-05-04 16:36', '1997-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpMPDMIB.setRevisionsDescriptions(('Updated addresses, published as RFC 3412.', 'Updated addresses, published as RFC 2572.', 'Original version, published as RFC 2272.',))
if mibBuilder.loadTexts: snmpMPDMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpMPDMIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpMPDMIB.setContactInfo('WG-EMail:   snmpv3@lists.tislabs.com\n                  Subscribe:  snmpv3-request@lists.tislabs.com\n\n                  Co-Chair:   Russ Mundy\n                              Network Associates Laboratories\n                  postal:     15204 Omega Drive, Suite 300\n                              Rockville, MD 20850-4601\n                              USA\n\n                  EMail:      mundy@tislabs.com\n                  phone:      +1 301-947-7107\n\n                  Co-Chair &\n                  Co-editor:  David Harrington\n                              Enterasys Networks\n                  postal:     35 Industrial Way\n                              P. O. Box 5005\n                              Rochester NH 03866-5005\n                              USA\n                  EMail:      dbh@enterasys.com\n                  phone:      +1 603-337-2614\n\n                  Co-editor:  Jeffrey Case\n                              SNMP Research, Inc.\n                  postal:     3001 Kimberlin Heights Road\n                              Knoxville, TN 37920-9716\n                              USA\n                  EMail:      case@snmp.com\n                  phone:      +1 423-573-1434\n\n                  Co-editor:  Randy Presuhn\n                              BMC Software, Inc.\n                  postal:     2141 North First Street\n                              San Jose, CA 95131\n                              USA\n                  EMail:      randy_presuhn@bmc.com\n                  phone:      +1 408-546-1006\n\n                  Co-editor:  Bert Wijnen\n                              Lucent Technologies\n                  postal:     Schagen 33\n                              3461 GL Linschoten\n                              Netherlands\n                  EMail:      bwijnen@lucent.com\n                  phone:      +31 348-680-485\n                 ')
if mibBuilder.loadTexts: snmpMPDMIB.setDescription('The MIB for Message Processing and Dispatching\n\n                  Copyright (C) The Internet Society (2002). This\n                  version of this MIB module is part of RFC 3412;\n                  see the RFC itself for full legal notices.\n                 ')
snmpMPDAdmin = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 1))
snmpMPDMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2))
snmpMPDMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3))
snmpMPDStats = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2, 1))
snmpUnknownSecurityModels = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownSecurityModels.setStatus('current')
if mibBuilder.loadTexts: snmpUnknownSecurityModels.setDescription('The total number of packets received by the SNMP\n                 engine which were dropped because they referenced a\n                 securityModel that was not known to or supported by\n                 the SNMP engine.\n                ')
snmpInvalidMsgs = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInvalidMsgs.setStatus('current')
if mibBuilder.loadTexts: snmpInvalidMsgs.setDescription('The total number of packets received by the SNMP\n                 engine which were dropped because there were invalid\n                 or inconsistent components in the SNMP message.\n                ')
snmpUnknownPDUHandlers = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownPDUHandlers.setStatus('current')
if mibBuilder.loadTexts: snmpUnknownPDUHandlers.setDescription('The total number of packets received by the SNMP\n                 engine which were dropped because the PDU contained\n                 in the packet could not be passed to an application\n                 responsible for handling the pduType, e.g. no SNMP\n                 application had registered for the proper\n                 combination of the contextEngineID and the pduType.\n                ')
snmpMPDMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 1))
snmpMPDMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 2))
snmpMPDCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 11, 3, 1, 1)).setObjects(("SNMP-MPD-MIB", "snmpMPDGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpMPDCompliance = snmpMPDCompliance.setStatus('current')
if mibBuilder.loadTexts: snmpMPDCompliance.setDescription('The compliance statement for SNMP entities which\n                 implement the SNMP-MPD-MIB.\n                ')
snmpMPDGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 11, 3, 2, 1)).setObjects(("SNMP-MPD-MIB", "snmpUnknownSecurityModels"), ("SNMP-MPD-MIB", "snmpInvalidMsgs"), ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpMPDGroup = snmpMPDGroup.setStatus('current')
if mibBuilder.loadTexts: snmpMPDGroup.setDescription('A collection of objects providing for remote\n                 monitoring of the SNMP Message Processing and\n                 Dispatching process.\n                ')
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpMPDCompliance=snmpMPDCompliance, snmpMPDMIBConformance=snmpMPDMIBConformance, snmpMPDAdmin=snmpMPDAdmin, snmpMPDGroup=snmpMPDGroup, PYSNMP_MODULE_ID=snmpMPDMIB, snmpMPDMIBObjects=snmpMPDMIBObjects, snmpMPDMIBCompliances=snmpMPDMIBCompliances, snmpMPDMIBGroups=snmpMPDMIBGroups, snmpMPDMIB=snmpMPDMIB, snmpUnknownPDUHandlers=snmpUnknownPDUHandlers, snmpMPDStats=snmpMPDStats, snmpInvalidMsgs=snmpInvalidMsgs, snmpUnknownSecurityModels=snmpUnknownSecurityModels)

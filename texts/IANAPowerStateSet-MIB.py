#
# PySNMP MIB module IANAPowerStateSet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANAPowerStateSet-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:17:23 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, iso, TimeTicks, mib_2, Bits, MibIdentifier, IpAddress, NotificationType, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "iso", "TimeTicks", "mib-2", "Bits", "MibIdentifier", "IpAddress", "NotificationType", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaPowerStateSet = ModuleIdentity((1, 3, 6, 1, 2, 1, 228))
ianaPowerStateSet.setRevisions(('2015-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaPowerStateSet.setRevisionsDescriptions(('Initial version of this MIB module, as published as RFC\n        7460.',))
if mibBuilder.loadTexts: ianaPowerStateSet.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaPowerStateSet.setOrganization('IANA')
if mibBuilder.loadTexts: ianaPowerStateSet.setContactInfo('\n                  Internet Assigned Numbers Authority\n                  Postal: ICANN\n                  12025 Waterfront Drive, Suite 300\n                  Los Angeles, CA 90094\n                  United States\n                  Tel: +1-310-301 5800\n                  EMail: iana@iana.org')
if mibBuilder.loadTexts: ianaPowerStateSet.setDescription("Copyright (c) 2015 IETF Trust and the persons identified as\n        authors of the code.  All rights reserved.\n\n        Redistribution and use in source and binary forms, with or\n        without modification, is permitted pursuant to, and subject\n        to the license terms contained in, the Simplified BSD License\n        set forth in Section 4.c of the IETF Trust's Legal Provisions\n        Relating to IETF Documents\n        (http://trustee.ietf.org/license-info).\n\n        This MIB module defines the PowerStateSet Textual\n        Convention, which specifies the Power State Sets and\n        Power State Set Values an Energy Object supports.\n\n        The initial version of this MIB module was published in\n        RFC 7460; for full legal notices see the RFC itself.")
class PowerStateSet(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/power-state-sets'
    description = 'IANAPowerState is a textual convention that describes\n        Power State Sets and Power State Set Values an Energy\n        Object supports.  IANA has created a registry of Power\n        State supported by an Energy Object and IANA shall\n        administer the list of Power State Sets and Power\n        States.\n\n        The Textual Convention assumes that Power States in a\n        Power State Set are limited to 255 distinct values.  For\n        a Power State Set S, the named number with the value S *\n        256 is allocated to indicate the Power State Set.  For a\n        Power State X in the Power State Set S, the named number\n        with the value S * 256 + X + 1 is allocated to represent\n        the Power State.\n\n        Requests for new values should be made to IANA via email\n        (iana@iana.org).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 255, 256, 257, 258, 259, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036))
    namedValues = NamedValues(("other", 0), ("unknown", 255), ("ieee1621", 256), ("ieee1621Off", 257), ("ieee1621Sleep", 258), ("ieee1621On", 259), ("dmtf", 512), ("dmtfOn", 513), ("dmtfSleepLight", 514), ("dmtfSleepDeep", 515), ("dmtfOffHard", 516), ("dmtfOffSoft", 517), ("dmtfHibernate", 518), ("dmtfPowerOffSoft", 519), ("dmtfPowerOffHard", 520), ("dmtfMasterBusReset", 521), ("dmtfDiagnosticInterrapt", 522), ("dmtfOffSoftGraceful", 523), ("dmtfOffHardGraceful", 524), ("dmtfMasterBusResetGraceful", 525), ("dmtfPowerCycleOffSoftGraceful", 526), ("dmtfPowerCycleHardGraceful", 527), ("eman", 1024), ("emanMechOff", 1025), ("emanSoftOff", 1026), ("emanHibernate", 1027), ("emanSleep", 1028), ("emanStandby", 1029), ("emanReady", 1030), ("emanLowMinus", 1031), ("emanLow", 1032), ("emanMediumMinus", 1033), ("emanMedium", 1034), ("emanHighMinus", 1035), ("emanHigh", 1036))

mibBuilder.exportSymbols("IANAPowerStateSet-MIB", ianaPowerStateSet=ianaPowerStateSet, PowerStateSet=PowerStateSet, PYSNMP_MODULE_ID=ianaPowerStateSet)
